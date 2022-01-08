# -*- coding: utf-8 -*-
import docker

client = docker.from_env()

# 컨테이너 관리 소스
class containers_service:
    # 컨테이너 정지
    def stop(dockerid):
        client.containers.get(dockerid).stop()

    # 컨테이너 강제 종료
    def kill(dockerid):
        client.containers.get(dockerid).kill()
    
    # 컨테이너 삭제
    def remove(dockerid):
        container = client.containers.get(dockerid)
        container.stop()
        container.remove()

    # 컨테이너 재시작
    def restart(dockerid):
        client.containers.get(dockerid).restart()

    # 컨테이너 시작
    def start(dockerid):
        client.containers.get(dockerid).start()