#!/usr/bin/env python
#Facebook Tray Application - A simple gnome applet for displaying/accessing facebook notifications
#Copyright (C) 2009 Matt Katzenberger (mattkatzen+facebook@gmail.com)
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import urllib
import xmllib


#You MUST get and use your own RSS feeds from facebook.
#The Notifications feed can be found by going to www.new.facebook.com/notifications.php and subscribing to the notifications RSS feed.

HOST = "www.new.facebook.com"
NOTIFY_PATH = "" #add everything after www.new.facebook.com for your rss feed in these quotes.
#eg NOTIFY_PATH = "/feeds/notifications.php?id=123456789&viewer=123456789&key=98abc76543&format=rss20"
FRIEND_STATUS_PATH =""  #add everything after www.new.facebook.com for your rss feed in these quotes.
#eg FRIEND_STATUS_PATH ="/feeds/friends_status.php?id=123456789&key=a1234567b8&format=rss20"

print "\n"

print "Getting Notifications"
file = urllib.urlopen("http://" + HOST + NOTIFY_PATH)
notifications = file.read()

print "Getting Friend Status Updates"
file = urllib.urlopen("http://" + HOST + FRIEND_STATUS_PATH)
friend_status = file.read()

print "notifications", len(notifications), "bytes"
print "friend statuses", len(friend_status), "bytes"

print "Creating notifications.rss"
notification_rss = open("notifications.rss", "w")
notification_rss.write(notifications)
notification_rss.close()

print "Create friend_status.rss"
friend_status_rss = open("friend_status.rss", "w")
friend_status_rss.write(friend_status)
friend_status_rss.close()

print "Closing...\n"



class rss_parser(xmllib.XMLParser):

    data = ""

    def start_title(self, attr):
        self.data = ""

    def end_title(self):
        print "TITLE:\t", repr(self.data)
        
    def start_link(self, attr):
        self.data = ""

    def end_link(self):
        print "LINK:\t", repr(self.data)

    def start_pubDate(self, attr):
        self.data = ""

    def end_pubDate(self):
        print "DATE:\t", repr(self.data),"\n"

    def handle_data(self, data):
        self.data = self.data + data
    	
import sys

parser = rss_parser()
parser.feed(notifications)
parser.close()

print "\n"

parser = rss_parser()
parser.feed(friend_status)
parser.close()

