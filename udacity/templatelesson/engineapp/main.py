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
import jinja2
import os

templateDir=os.path.join(os.path.dirname(__file__),'templates')
jinjaEnv=jinja2.Environment(loader=jinja2.FileSystemLoader(templateDir))


class Handler(webapp2.RequestHandler):
    def write(self,*a,**kw):
        self.response.out.write(*a,**kw)
    def renderStr(self,template,**params):
        t=jinjaEnv.get_template(template)
        return t.render(params)
    def render(self,template,**params):
        self.write(self.renderStr(template,**params))

class MainHandler(Handler):
    def get(self):
        n=self.request.get('n')
        if n:
            n=int(n)
        self.render('shoppingList.html',n=n)
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
