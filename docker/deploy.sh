#!/bin/bash
set -e

echo ">>>>>>> copying a correct compose file <<<<<<<"
scp -o "StrictHostKeyChecking no" docker/docker-compose.${PROJECT_PROFILE}.yml \
    ${REMOTE_USER}@${REMOTE_HOST}:${PROJECT_DIR}/${PROJECT_PROFILE}/docker-compose.yml

echo ">>>>>>> copying a environment file <<<<<<<"
scp -o "StrictHostKeyChecking no" docker/${PROJECT_PROFILE}/.env_file \
    ${REMOTE_USER}@${REMOTE_HOST}:${PROJECT_DIR}/${PROJECT_PROFILE}/.env

echo ">>>>>>> copying a nginx conf file <<<<<<<"
scp -o "StrictHostKeyChecking no" docker/${PROJECT_PROFILE}/conf.nginx \
    ${REMOTE_USER}@${REMOTE_HOST}:${PROJECT_DIR}/${PROJECT_PROFILE}/conf.nginx

COMPOSE_OPTS="-f ./docker-compose.yml -p VR_${PROJECT_PROFILE}"

#    docker login -u $DOCKER_LOGIN -p $DOCKER_PASSWORD
#    echo $DOCKER_PASSWORD | docker login registry.gitlab.com --username=$DOCKER_LOGIN --password-stdin

echo ">>>>>>> starting containers on the remote server <<<<<<<"
ssh ${REMOTE_USER}@${REMOTE_HOST} -o "StrictHostKeyChecking no" << EOF
    cd ${PROJECT_DIR}/${PROJECT_PROFILE}

    echo ">>>>>>> docker-compose pull/down/up <<<<<<<"
    docker-compose ${COMPOSE_OPTS} pull
    docker-compose ${COMPOSE_OPTS} down
    docker-compose ${COMPOSE_OPTS} up -d


EOF

echo "Done!"
exit 0
