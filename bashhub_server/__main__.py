# flake8: noqa

from asphalt.core.runner import run_application

run_application(component={
    "type": "bashhub_server.container:AppContainer"
})
