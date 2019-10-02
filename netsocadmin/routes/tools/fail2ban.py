# stdlib
import logging

# lib
import flask

# local
import help_post

from .index import AdminToolView


class Fail2BanView(AdminToolView):
    """
    Route: fail2ban
    """
    template_file = "fail2ban.html"

    page_title = "Fail2Ban"

    active = "fail2ban"
    # Logger instance
    logger = logging.getLogger("netsocadmin.fail2ban")

    def dispatch_request(self) -> str:
        server = flask.request.args.get("server", "leela")

        return self.render(server=server)
