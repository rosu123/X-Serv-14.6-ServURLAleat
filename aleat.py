#!/usr/bin/python3

import webapp


class URLAleat(webapp.webApp):
    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """
        import random
        return ("200 OK", "<html><body><h1><a href='" +
                str(random.randint(1, 100000)) +
                "'>Dame otra!</a></h1></body></html>")


if __name__ == "__main__":
    testWebApp = URLAleat("localhost", 1234)
