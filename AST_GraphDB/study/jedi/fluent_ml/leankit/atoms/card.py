from automation.core.utils import objectpath_wrapper
from automation.core.datastore.tinydb_datastore import DataStore
from automation.integration.src.time_testcase_helper import TimeTestCaseHelper
from automation.fluent_ml.leankit.features.card import Card
from automation.fluent_ml.leankit.atoms.artifact import Leankit
from automation.fluent_ml.leankit.features.board import Board
from automation.fluent_ml.leankit.features.lk_verify import LKVerify


class CardAtom(Leankit):
    def __init__(self, name=None, board='board1'):
        super().__init__()
        self.payload_update = []
        self.payload_move = {}
        self.card = Card()
        self.table_name = self.card.tbl_name
        self.verify = LKVerify()
        self.card_id = self._get_card_id(name, board)
        self.board = board

    def _get_card_id(self, name, board):
        if name:
            card_details = DataStore.read('LK_Card', name=name)
            if card_details:
                card_id = card_details['id']
            else:
                card_id = self.create(name, board)
            return card_id

    def create(self, name, board='board1'):
        self.board = board
        board_id = self.lk_constants[board]['id']
        card_type = self.lk_constants[board]['card_type']['default']

        payload_create = {'boardId': board_id, 'typeId': card_type, 'title': name}
        card_id = self.card.create(payload_create)
        return card_id

    def create_child_card(self, name, board='board1'):
        parent_id = self.card_id
        board_id = self.lk_constants[board]['id']
        card_type = self.lk_constants[board]['card_type']['default']

        payload_create = {'boardId': board_id, 'typeId': card_type, 'title': name,
                          'connections': {'parents': [parent_id]}}
        self.card.create(payload_create)
        return self

    def create_multiple_child_cards(self, lst_names, board='board1'):
        parent_id = self.card_id
        board_id = self.lk_constants[board]['id']
        card_type = self.lk_constants[board]['card_type']['default']

        for name in lst_names:
            payload_create = {'boardId': board_id, 'typeId': card_type, 'title': name,
                              'connections': {'parents': [parent_id]}}
            self.card.create(payload_create)
        return self

    def goto_card(self, name, board='board1'):
        card_details = DataStore.read(self.table_name, name=name)
        self.card_id = card_details['id']
        self.board = board
        return self

    def update(self):
        self.card.update(self.card_id, self.payload_update)
        self.payload_update = []
        return self

    def update_description(self, description):
        payload_update = [{'op': 'replace', 'path': '/description', 'value': description}]
        self.card.update(self.card_id, payload_update)
        return self

    def update_title(self, new_title):
        payload_update = [{'op': 'add', 'path': '/title', 'value': new_title}]
        self.card.update(self.card_id, payload_update)
        return self

    def move_to_board(self, board):
        # card_details = DataStore.read(self.table_name, name=name)
        card_id = self.card_id
        board_id = self.lk_constants[board]['id']

        payload = {'cardIds': [card_id], 'destination': {'boardId': board_id}}
        self.card.move(card_id, payload)
        return self

    def move_to_connected_cards_done_lane(self):
        card_id = self.card_id

        lane_id = self.lk_constants['board2']['connected_cards_done_lane']
        payload = {'cardIds': [card_id], 'destination': {'laneId': lane_id}}

        self.card.move(card_id, payload)
        return self

    def delete_description(self):
        # card_details = DataStore.read(self.table_name, name=name)
        card_id = self.card_id

        payload_update = [{'op': 'replace', 'path': '/description', 'value': ''}]
        self.card.update(card_id, payload_update)
        return self

    def delete(self):
        card_id = self.card_id
        setattr(CardAtom, 'deleted_card_id', card_id)
        self.card.delete(card_id)
        return self

    def exists(self):
        # card_details = DataStore.read('LK_Card', name=name)
        # card_id = card_details['id']
        self.verify.card_details(self.card_id, {})
        return self

    def not_exists(self):
        card_id = getattr(CardAtom, 'deleted_card_id')
        self.card.verify_delete(card_id)
        return self

    def set_title(self, title):
        payload_name = {'op': 'add', 'path': '/title', 'value': title}
        self.payload_update.append(payload_name)
        return self

    def set_planned_start(self, planned_start_date):
        """
        planned_start_date: should be in format - 'YYYY-MM-DD'
        """
        planned_start = {'op': 'add', 'path': '/plannedStart', 'value': planned_start_date}
        self.payload_update.append(planned_start)
        return self

    def set_planned_finish(self, planned_finish_date):
        """
        planned_finish_date: should be in format - 'YYYY-MM-DD'
        """
        planned_finish = {'op': 'add', 'path': '/plannedFinish', 'value': planned_finish_date}
        self.payload_update.append(planned_finish)
        return self

    def unset_planned_start(self):
        payload = {'op': 'remove', 'path': '/plannedStart', 'value': None}
        self.payload_update.append(payload)
        return self

    def unset_planned_finish(self):
        payload = {'op': 'remove', 'path': '/plannedFinish', 'value': None}
        self.payload_update.append(payload)
        return self

    def set_size(self, size):
        payload_size = {'op': 'replace', 'path': '/size', 'value': size}
        self.payload_update.append(payload_size)
        return self

    def set_lane(self, lane_name):
        lane_id = self.lk_constants[self.board]['lane_name'][lane_name]
        payload_lane = {'op': 'replace', 'path': '/laneId', 'value': lane_id}
        self.payload_update.append(payload_lane)
        return self

    def set_priority(self, priority):
        payload_lane = {'op': 'replace', 'path': '/priority', 'value': priority}
        self.payload_update.append(payload_lane)
        return self

    def set_card_type(self, card_type):
        type_id = self.lk_constants['board1']['card_type'][card_type]
        payload_lane = {'op': 'replace', 'path': '/typeId', 'value': type_id}
        self.payload_update.append(payload_lane)
        return self

    def set_blocked_flag(self, is_blocked):
        blocked_reason = None
        if is_blocked:
            blocked_reason = 'PRM PP Integration'

        payload_lane = [{'op': 'replace', 'path': '/isBlocked', 'value': is_blocked},
                        {'op': 'replace', 'path': '/blockReason', 'value': blocked_reason}]
        self.payload_update.extend(payload_lane)
        return self

    def verify_details(self):
        card_id = self.card_id
        card_details = DataStore.read('LK_Card', id=card_id)
        board_id = card_details['boardId']
        name = card_details['name']

        dct_expected = {'title': name, 'boardId': board_id}
        self.verify.card_details(card_id, dct_expected)
        return self

    def verify_default_top_lane(self):
        exp_default_lane = self.lk_constants['board1']['default_lane_id']

        # card_details = DataStore.read(self.table_name, name=name)
        card_id = self.card_id

        dct_expected = {'laneId': exp_default_lane}
        self.verify.card_details(card_id, dct_expected)
        return self

    def verify_top_lane(self, lane_name):
        dct_lane_details = self.lk_constants['board1']['lane_name']
        lane_id = dct_lane_details[lane_name]

        # card_details = DataStore.read(self.table_name, name=name)
        card_id = self.card_id

        dct_expected = {'laneId': lane_id}
        self.verify.card_details(card_id, dct_expected)
        return self

    def verify_creator(self, card_creator):
        # card_details = DataStore.read('LK_Card', name=name)
        card_id = self.card_id

        dct_expected = {'createdBy': card_creator}
        self.verify.card_details(card_id, dct_expected)
        return self

    def verify_planned_start(self, planned_start):
        """
        planned_start: has format 2018-10-09T08:00:00 or 2018-10-09
        """
        # card_details = DataStore.read('LK_Card', name=name)
        card_id = self.card_id

        planned_start = TimeTestCaseHelper.data_formatter_leankit(planned_start)

        dct_expected = {'plannedStart': planned_start}
        self.verify.card_details(card_id, dct_expected)
        return self

    def verify_planned_finish(self, planned_finish):
        """
        planned_finish: has format 2018-10-09T17:00:00 or 2018-10-09
        """
        # card_details = DataStore.read('LK_Card', name=name)
        card_id = self.card_id

        planned_finish = TimeTestCaseHelper.data_formatter_leankit(planned_finish)

        dct_expected = {'plannedFinish': planned_finish}
        self.verify.card_details(card_id, dct_expected)
        return self

    def verify_description(self, description):
        # card_details = DataStore.read('LK_Card', name=name)
        card_id = self.card_id

        dct_expected = {'description': description}
        self.verify.card_details(card_id, dct_expected)
        return self

    def verify_card_type(self, card_type='default'):
        card_id = self.card_id
        card_type_id = self.lk_constants[self.board]['card_type'][card_type]

        dct_expected = {'typeId': card_type_id}
        self.verify.card_details(card_id, dct_expected)
        return self

    def get_default_lane_id(self, board='board1'):
        board_id = self.lk_constants[board]['id']
        board_obj = Board()
        read_resp = board_obj.read(board_id)
        default_lane_id = objectpath_wrapper.filter_dct_for_key('isDefaultDropLane', True, 'id',
                                                                read_resp.json())[0]
        return default_lane_id

    def get_earliest_actual_start(self, name):
        """
        returns: date in format: 2018-10-04T06:01:58Z
        """
        card_details = DataStore.read('LK_Card', name=name)
        card_id = card_details['id']
        read_resp = self.card.read(card_id).json()

        earliest_actual_start_key = 'connectedCardStats.actualStart'
        earliest_actual_start_date = objectpath_wrapper.get_dct_value(earliest_actual_start_key, read_resp)
        earliest_actual_start_date = earliest_actual_start_date[0] if earliest_actual_start_date else None
        return earliest_actual_start_date

    def get_latest_actual_finish(self, name):
        """
        returns: date in format: 2018-10-04T06:01:58Z
        """
        card_details = DataStore.read('LK_Card', name=name)
        card_id = card_details['id']
        read_resp = self.card.read(card_id).json()

        latest_actual_finish_key = 'connectedCardStats.actualFinish'
        latest_actual_finish_date = objectpath_wrapper.get_dct_value(latest_actual_finish_key, read_resp)
        latest_actual_finish_date = latest_actual_finish_date[0] if latest_actual_finish_date else None
        return latest_actual_finish_date

    def get_actual_start(self, name):
        """
        returns: date in format: 2018-10-04T06:01:58Z
        """
        card_details = DataStore.read('LK_Card', name=name)
        card_id = card_details['id']
        read_resp = self.card.read(card_id).json()

        actual_start_key = 'actualStart'
        actual_start_date = objectpath_wrapper.get_dct_value(actual_start_key, read_resp)
        actual_start_date = actual_start_date[0] if actual_start_date else None
        return actual_start_date

    def get_actual_finish(self, name):
        """
        returns: date in format: 2018-10-04T06:01:58Z
        """
        card_details = DataStore.read('LK_Card', name=name)
        card_id = card_details['id']
        read_resp = self.card.read(card_id).json()

        actual_finish_key = 'actualFinish'
        actual_finish_date = objectpath_wrapper.get_dct_value(actual_finish_key, read_resp)
        actual_finish_date = actual_finish_date[0] if actual_finish_date else None
        return actual_finish_date

    def verify_title(self, name):
        card_id = self.card_id

        dct_expected = {'title': name}
        self.verify.card_details(card_id, dct_expected)
        return self

    def teardown(self, scope):
        lst_record = DataStore.read_by_scope(self.table_name, scope=scope)
        for record in lst_record:
            card_id = record['id']
            self.card.delete(card_id)
        return self
