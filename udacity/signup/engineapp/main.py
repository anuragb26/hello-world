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
import re
import urllib


form = '''
            <h2>Signup</h2>
            <form method="post">
            <table>
                <tbody>
                <tr>
                        <td class="label">
                        Username
                        </td>
                        <td>
                            <input type="text" name="username" value="{userName}">
                        </td>
                        <td style="color:red;">{userNameErr}</td>
                </tr>

                <tr>
                      <td class="label">
                        Password
                      </td>
                      <td>
                        <input type="password" name="password" value="{password}">
                      </td>
                      <td style="color:red;">{password2Err}</td>
                </tr>

                <tr>
                      <td class="label">
                        Verify Password
                      </td>
                      <td>
                        <input type="password" name="verify" value="{verify}">
                      </td>
                      <td style="color:red;">{password1Err}</td>
                </tr>

                <tr>
                      <td class="label">
                        Email (optional)
                      </td>
                      <td>
                        <input type="text" name="email" value="{email}">
                      </td>
                      <td style="color:red;">{emailErr}</td>
                </tr>
                </tbody>
            </table>
      <input type="submit">
    </form>    

        '''
welcomeMarkup = '''
              <h2>Welcome, {0}!</h2>  
              '''
class MainHandler(webapp2.RequestHandler):
    def writeHtml(self,markup,formData):
        self.response.out.write(markup.format(**formData))
    def verifyFormData(self,formData):
        errorInfo={
                    'userNameErr':"",
                    'password1Err':"",
                    'password2Err':"",
                    'emailErr':""
                  }
        userName=re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        password=re.compile(r"^.{3,20}$")
        email=re.compile(r"^[\S]+@[\S]+.[\S]+$")
        if userName.match(formData['userName']) is  None:
        	self.response.out.write(str(userName.match(formData['userName'])))
        	errorInfo['userNameErr']="That's not a valid username"
        if password.match(formData['password']) is not None:
        	if formData['password'] != formData['verify']:
        		errorInfo['password1Err']="Your passwords didn't match."
        else:
        	errorInfo['password2Err']="That wasn't a valid password."
        if formData['email'] != '': 
        	if email.match(formData['email']) is None:
        		errorInfo['emailErr']="That's not a valid email."
        return errorInfo
    def get(self):
        errorInfo={
                    'userNameErr':"",
                    'password1Err':"",
                    'password2Err':"",
                    'emailErr':""
                  }
        formData={
                    'userName':"",
                    'password':"",
                    'verify':"",
                    'email':""
                  } 
        formData.update(errorInfo)
        self.writeHtml(form,formData)
    def post(self):
        formData={}
        formData['userName']=self.request.get('username')
        formData['password']=self.request.get('password')
        formData['verify']=self.request.get('verify')
        formData['email']=self.request.get('email')
        errorInfo=self.verifyFormData(formData)
        if(any(errorInfo.values())):
       		formData['password']=""
        	formData['verify']=""
        	formData.update(errorInfo)
        	self.writeHtml(form,formData)
        else:
            queryParam={"username":formData['userName']}
            url="/welcome?"+urllib.urlencode(queryParam)
            self.redirect(url)   
        
class WelcomeHandler(webapp2.RequestHandler):
    def writeHtml(self,htmlMarkup,userName):
        self.response.out.write(htmlMarkup.format(userName))              
    def get(self):
        userName=self.request.get('username')
        self.writeHtml(welcomeMarkup,userName)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome',WelcomeHandler)                    
], debug=True)
