import sublime, sublime_plugin

class ToggleNightAndDayCommand(sublime_plugin.ApplicationCommand):
   def run(self, **args):
        settings = sublime.load_settings('Preferences.sublime-settings')

        nightAndDay = sublime.load_settings('Night and Day.sublime-settings')
        dayTheme    = nightAndDay.get("day_theme",    "")
        dayScheme   = nightAndDay.get("day_scheme",   "")
        nightTheme  = nightAndDay.get("night_theme",  "")
        nightScheme = nightAndDay.get("night_scheme", "")

        if( nightTheme  != "" and
            nightTheme  != settings.get("theme",        "") or
            nightScheme != settings.get("color_scheme", "")):
            if nightTheme  != "" : settings.set("theme",        nightTheme )
            if nightScheme != "" : settings.set("color_scheme", nightScheme)
            sublime.status_message('Night mode')
        else :
            if dayTheme  != "" : settings.set("theme",        dayTheme )
            if dayScheme != "" : settings.set("color_scheme", dayScheme)
            sublime.status_message('Day mode')

        sublime.save_settings('Preferences.sublime-settings')