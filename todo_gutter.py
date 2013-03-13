import sublime
import sublime_plugin


class TodoGutterCommand(sublime_plugin.EventListener):
    icon = '../TodoGutter/exclamation'
    region_names = ['todo']

    def clear_regions(self, view):
        for region_name in self.region_names:
            view.erase_regions('todo_gutter_%s' % region_name)

    def find_todos(self, view):
        regions = []
        settings = sublime.load_settings('TodoGutter.sublime-settings')
        todo_regexes = settings.get('todo_regexes')
        for regex in todo_regexes:
            regions.extend(view.find_all(regex))
        return regions

    def on_load(self, view):
        self.show_icons(view)

    def on_post_save(self, view):
        self.show_icons(view)

    def show_icons(self, view):
        self.clear_regions(view)
        regions = self.find_todos(view)
        scope = 'string'
        view.add_regions('todo_gutter_todo', regions, scope, self.icon, sublime.HIDDEN)
