import sublime
import sublime_plugin
import base64
import urllib.parse

class Base16EncodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                selected_text = self.view.substr(region)
                try:
                    encoded_text = base64.b16encode(selected_text.encode()).decode()
                    self.view.replace(edit, region, encoded_text)
                except Exception as e:
                    error_message = "Base16 Encoding Error: {}".format(str(e))
                    sublime.message_dialog(error_message)

class Base16DecodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                selected_text = self.view.substr(region)
                try:
                    decoded_text = base64.b16decode(selected_text.encode()).decode()
                    self.view.replace(edit, region, decoded_text)
                except Exception as e:
                    error_message = "Base16 Decoding Error: {}".format(str(e))
                    sublime.message_dialog(error_message)

class Base32EncodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                selected_text = self.view.substr(region)
                try:
                    encoded_text = base64.b32encode(selected_text.encode()).decode()
                    self.view.replace(edit, region, encoded_text)
                except Exception as e:
                    error_message = "Base32 Encoding Error: {}".format(str(e))
                    sublime.message_dialog(error_message)

class Base32DecodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                selected_text = self.view.substr(region)
                try:
                    decoded_text = base64.b32decode(selected_text.encode()).decode()
                    self.view.replace(edit, region, decoded_text)
                except Exception as e:
                    error_message = "Base32 Decoding Error: {}".format(str(e))
                    sublime.message_dialog(error_message)

class Base64EncodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                selected_text = self.view.substr(region)
                try:
                    encoded_text = base64.b64encode(selected_text.encode()).decode()
                    self.view.replace(edit, region, encoded_text)
                except Exception as e:
                    error_message = "Base64 Encoding Error: {}".format(str(e))
                    sublime.message_dialog(error_message)

class Base64DecodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                selected_text = self.view.substr(region)
                try:
                    decoded_text = base64.b64decode(selected_text.encode()).decode()
                    self.view.replace(edit, region, decoded_text)
                except Exception as e:
                    error_message = "Base64 Decoding Error: {}".format(str(e))
                    sublime.message_dialog(error_message)

class UrlEncodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                selected_text = self.view.substr(region)
                try:
                    encoded_text = urllib.parse.quote(selected_text)
                    self.view.replace(edit, region, encoded_text)
                except Exception as e:
                    error_message = "URL Encoding Error: {}".format(str(e))
                    sublime.message_dialog(error_message)

class UrlDecodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                selected_text = self.view.substr(region)
                try:
                    decoded_text = urllib.parse.unquote(selected_text)
                    self.view.replace(edit, region, decoded_text)
                except Exception as e:
                    error_message = "URL Decoding Error: {}".format(str(e))
                    sublime.message_dialog(error_message)

