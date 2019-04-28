from automation.core.datastore.tinydb_datastore import DataStore
from automation.fluent_ml.leankit.atoms.artifact import Leankit
from automation.fluent_ml.leankit.features.card import Card
from automation.fluent_ml.leankit.features.board import Board


class BoardAtom(Leankit):
    def __init__(self):
        super().__init__()
        self.board_obj = Board()

    def update_lane_to_connected_cards_done(self, lane, board, flag=True):
        payload = {'isConnectionDoneLane': flag}
        board_id = self.lk_constants[board]['id']
        lane_id = self.lk_constants[board]['lane_name'][lane]

        self.board_obj.update(board_id, lane_id, payload)
        return self

