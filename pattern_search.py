import subprocess


class PatternSearcher:
    def __init__(self):
        self.batch_file = r'D:\Batch_Files\find_pattern.bat'
        # self.regex_pat = regex_pattern
        # self.file_name = file_name


    def local_run(self, err_id):
        # my_bat = r'D:\Batch_Files\find_pattern.bat'
        regex_pat = r".*PveIntegErr_{0}".format(err_id)
        file_name = r'D:\Temp\ProjectPlace_Integration_Detailed_Log.Log'
        _cmd = "{0}  {1}  {2}".format(self.batch_file, regex_pat, file_name)
        self.execute_cmd(_cmd)

    def remote_run(self):
        # my_bat = r'D:\Batch_Files\find_pattern.bat'
        regex_pat = r"1.42"
        file_name = r'C:\Rally_Config.ini'
        _cmd = r'psexec \\10.132.16.2 -u corporate\qainstaller -p p@ssw0rd -c {0} {1} {2}'.format(self.batch_file,
                                                                                                        regex_pat,
                                                                                                        file_name)

        self.execute_cmd(_cmd)

    def execute_cmd(self, _cmd):
        proc = subprocess.Popen(_cmd, stdin=None, stderr=None, shell=False)
        proc.communicate(input=None)
        if proc.returncode == 0:
            print('\n Pattern search was successful\n')
            self.status = True
        else:
            print('Error code', proc.returncode)
            print('\n Pattern search was not successful\n')
        print('-----', proc.returncode)



if __name__ == '__main__':
    client_obj = PatternSearcher()
    # client_obj.local_run(96)

    client_obj.remote_run()
