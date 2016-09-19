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

form='''
<form method = "post" >
    What is your birthday ?
    <br>
    <label>Month <input type="text" name="month" value="{monInput}"></label>
    <label>Day <input type="text" name = "day" value = "{dayInput}"></label>
    <label>Year <input type = "text" name = "year" value = "{yearInput}"></label>
    <div style="color:red">{error}</div>
    <br>
    <br>
    <input type="submit">
</form>
'''
import webapp2
import cgi
months=['January','February','March','April','May','June','July','August','September','October','November','December']
monthsDict={m[:3].lower():m for m in months}

def validMonth(mon):
        m=mon[:3].lower()
        return monthsDict.get(m)
        
def validDay(day):
    if day and day.isdigit():
        d=int(day)
        if d > 0 and d < 32:
            return d
def validYear(year):
    if year and year.isdigit():
        y=int(year)
        if(y > 1900 and y < 2020):
            return y
        
def escapeHtml(s):
    return cgi.escape(s,quote=True)
        
class MainHandler(webapp2.RequestHandler):
    def writeForm(self,error="",monInput="",dayInput="",yearInput=""):
        self.response.out.write(form.format(error=error,monInput=escapeHtml(monInput),dayInput=escapeHtml(dayInput),yearInput=escapeHtml(yearInput)))
    def get(self):
        self.response.headers['Content-type']='text/html'
        self.writeForm()
    def post(self):
        monInput=self.request.get('month')
        dayInput=self.request.get('day')
        yearInput=self.request.get('year')
        isValidMonth=validMonth(monInput)
        isValidDay=validDay(dayInput)
        isValidYear=validYear(yearInput)
        if(not(isValidMonth and isValidDay and isValidYear)):
            self.writeForm('There is some error',monInput,dayInput,yearInput)
        else:
            self.redirect('/thanks')
    
class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('You have entered valid data')
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/thanks',ThanksHandler)
], debug=True)
