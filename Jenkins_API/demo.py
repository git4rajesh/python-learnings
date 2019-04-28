from jenkinsapi.jenkins import Jenkins

class JenkinsClient:
    def __init__(self, jenkins_server):
        jenkins_url = 'http://{}:8080/'.format(jenkins_server)
        user_name = 'admin'
        password = 'admin'
        self.j_server = Jenkins(jenkins_url,user_name,password)

    def get_job_name(self):
        pass

    def get_job_handle(self, job_name):
        job_handle = self.j_server.get_job(job_name)
        return job_handle

    def get_job_build_number(self, job_handle):
        return job_handle.get_last_buildnumber()

    def get_run_id_param(self, job_handle):
        build = job_handle.get_last_build()
        parameters = build.get_actions()['parameters']
        run_id = parameters[0]['value']
        return run_id

    def get_job_duration(self, job_name):
        job_handle = self.get_job_handle(job_name)
        build_no = self.get_job_build_number(job_handle)
        for name, instance in self.j_server.get_jobs():
            if name == job_name:
                build_metadata = instance.get_build_metadata(build_no)
                total_time = build_metadata.get_duration().total_seconds()
                return total_time/60, total_time % 60


if __name__ == '__main__':
    jc = JenkinsClient('10.132.4.43')
    jh =jc.get_job_handle('01_Daily_Regression')
    print(jc.get_job_build_number(jh))
