import terminatorlib.plugin as plugin
import gtk
import webbrowser
AVAILABLE = ['GoogleOnMenu']
class GoogleOnMenu(plugin.MenuItem):
	capabilities = ['terminal_menu']
	def callback(self, menuitems, menu, terminal):
		google_item = gtk.MenuItem('Google')
		vte = terminal.get_vte()
		searchTerm = gtk.clipboard_get(gtk.gdk.SELECTION_PRIMARY).wait_for_text()
		google_item.connect("activate", self.googleIt, searchTerm)
		menuitems.append(google_item)
		#terminal.get_vte() gives access to vte terminal

	def googleIt(self, menuitem, searchTerm):
		url = "https://www.google.com/search?q=" + searchTerm
		webbrowser.open(url, 0, True)

