@echo off
echo Cleaning up Docker containers and cache...

REM Stop and remove any existing devcontainers
docker stop $(docker ps -q --filter "label=devcontainer.local_folder=c:\Projects\Assistant\khoj") 2>nul
docker rm $(docker ps -aq --filter "label=devcontainer.local_folder=c:\Projects\Assistant\khoj") 2>nul

REM Clean Docker build cache
docker builder prune -f
docker system prune -f

REM Remove any cached devcontainer images
docker rmi $(docker images -q --filter "label=devcontainer.local_folder=c:\Projects\Assistant\khoj") 2>nul

echo Docker cleanup complete!
echo Now try opening your project in Cursor again.
pause