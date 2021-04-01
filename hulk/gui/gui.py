# import sys

import webview

from hulk.bitbucket_manager import BitbucketManager

# html = """
# <!DOCTYPE html>
# <html>
# <head lang="en">
# <meta charset="UTF-8">
#
# <style>
#     #response-container {
#         display: none;
#         padding: 3rem;
#         margin: 3rem 5rem;
#         font-size: 120%;
#         border: 5px dashed #ccc;
#     }
#
#     label {
#         margin-left: 0.3rem;
#         margin-right: 0.3rem;
#     }
#
#     button {
#         font-size: 100%;
#         padding: 0.5rem;
#         margin: 0.3rem;
#         text-transform: uppercase;
#     }
#
# </style>
# </head>
# <body>
#
#
# <h1>JS API Example</h1>
# <p id='pywebview-status'><i>pywebview</i> is not ready</p>
#
# <button onClick="initialize()">Hello Python</button><br/>
# <button id="heavy-stuff-btn" onClick="doHeavyStuff()">Perform a heavy operation</button><br/>
# <button onClick="getRandomNumber()">Get a random number</button><br/>
# <label for="name_input">Say hello to:</label><input id="name_input" placeholder="put a name here">
# <button onClick="greet()">Greet</button><br/>
# <button onClick="catchException()">Catch Exception</button><br/>
#
#
# <div id="response-container"></div>
# <script>
#     window.addEventListener('pywebviewready', function() {
#         var container = document.getElementById('pywebview-status')
#         container.innerHTML = '<i>pywebview</i> is ready'
#     })
#
#     function showResponse(response) {
#         var container = document.getElementById('response-container')
#
#         container.innerText = response.message
#         container.style.display = 'block'
#     }
#
#     function initialize() {
#         pywebview.api.init().then(showResponse)
#     }
#
#     function doHeavyStuff() {
#         var btn = document.getElementById('heavy-stuff-btn')
#
#         pywebview.api.doHeavyStuff().then(function(response) {
#             showResponse(response)
#             btn.onclick = doHeavyStuff
#             btn.innerText = 'Perform a heavy operation'
#         })
#
#         showResponse({message: 'Working...'})
#         btn.innerText = 'Cancel the heavy operation'
#         btn.onclick = cancelHeavyStuff
#     }
#
#     function cancelHeavyStuff() {
#         pywebview.api.cancelHeavyStuff()
#     }
#
#     function getRandomNumber() {
#         pywebview.api.getRandomNumber().then(showResponse)
#     }
#
#     function greet() {
#         var name_input = document.getElementById('name_input').value;
#         pywebview.api.sayHelloTo(name_input).then(showResponse)
#     }
#
#     function catchException() {
#         pywebview.api.error().catch(showResponse)
#     }
#
# </script>
# </body>
# </html>
# """


class Api:
    """
    API of the serverless app to communicate JavaScript and Python
    """

    # def __init__(self):

    # def python_version(self):
    #     response = {
    #         'message': 'Python {0}'.format(sys.version)
    #     }
    #     return response
    #
    # def error(self):
    #     raise Exception('This is a Python exception')

    # def addItem(self, title):
    #     print('Added item %s' % title)
    #
    # def removeItem(self, item):
    #     print('Removed item %s' % item)
    #
    # def editItem(self, item):
    #     print('Edited item %s' % item)
    #
    # def toggleItem(self, item):
    #     print('Toggled item %s' % item)
    #
    # def toggleFullscreen(self):
    #     webview.windows[0].toggle_fullscreen()

    def login(self, username, password):
        """
        Login into Bitbucket account and list repos
        """
        print("HULK JS API - login")
        bb_man = BitbucketManager(username, password)
        try:
            bb_man.list_repos()
        except Exception as err:
            print("HULK JS API - login !!!", err)

    # def log(self, message):
    #     print("HULK JS API - " + message)


class App:
    """
    GUI of the app with the WebView
    """
    def __init__(self):
        api = Api()
        # window = webview.create_window('HULK', html=html, js_api=api)
        webview.create_window('HULK', 'assets/index.html', js_api=api)
        webview.start()


if __name__ == '__main__':
    app = App()
