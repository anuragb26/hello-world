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
import cgi

heading="<h2>Enter some text to ROT13:</h2>"
form='''
	 	<form method="post">
		<textarea name="text" style="height:100px;width:400px">{0}</textarea>
		<br>
		<input type="submit">
		</form>
		'''
alphabetLower='abcdefghijklmnopqrstuvwxyz'		
alphabetHigher=alphabetLower.upper()
strLen=len(alphabetLower)

def escapeHtml(c):
	return cgi.escape(c,quote=True)

class MainHandler(webapp2.RequestHandler):
	def writeHtml(self,htmlMarkup,content=""):
		self.response.out.write(htmlMarkup.format(content))

	def getUpdatedContent(self,content):
		newContent=[]
		for chr in content:
			if(chr in alphabetLower):
				c=alphabetLower[(alphabetLower.index(chr) + 13)%strLen]
			elif(chr in alphabetHigher):
				c=alphabetHigher[(alphabetHigher.index(chr) + 13)%strLen]
			else:
				c=escapeHtml(chr)	
			newContent.append(c)
		return "".join(newContent)
	def get(self):
		self.writeHtml(heading+form)

	def post(self):
		content=self.request.get('text')
		updatedContent=self.getUpdatedContent(content)
		self.writeHtml(heading+form,updatedContent)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
