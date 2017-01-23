#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random
#This code builds a dynamic website!!
def getRandomFortune():
    #list of possible fortune_sentence
    fortunes = [
    "I see much code in your future.",
    "Consider eating more fortune cookies.",
    "You have tamed the mighty Python, now you must free it onto the Great Spider's web.",
    "You future success cannot be believed."
    ]
    #randomly select one of the fortunes
    pickFortune = random.randint(0, 3)

    return fortunes[pickFortune]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"

        fortune = "<strong>" + getRandomFortune() + "</strong>"
        fortune_sentence = "Your fortune: " + fortune
        fortune_paragraph = "<p>" + fortune_sentence + "</p>"
        luckyNumber = "<strong>" + str(random.randint(1,100)) + "</strong>"
        number_sentence = 'Your lucky number is ' + luckyNumber
        number_paragraph = "<p>" + number_sentence + "</p>"
        cookie_button_again = "<a href = '.'><button>Another cookie please!</button></a>"
        content = header + fortune_paragraph + number_paragraph + cookie_button_again
        self.response.write(content)

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Thanks for trying to log in!")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', LoginHandler),
], debug=True)
