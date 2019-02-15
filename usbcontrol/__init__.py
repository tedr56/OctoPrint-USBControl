# coding=utf-8
from __future__                             import absolute_import
from subprocess import check_output
from subprocess import call
from octoprint.settings import settings, valid_boolean_trues
import octoprint.plugin
import os

class UsbcontrolPlugin(octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.AssetPlugin,
										 	 octoprint.plugin.SimpleApiPlugin,
											 octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin):

	def get_settings_defaults(self):
		return dict(
			usb2 =                                True,
			usb3 =                                True,
			usb4 =                                True,
			usb5 =                                True,
			init =                                False
		)

	def get_template_vars(self):
		return dict(
			usb2 =                                self._settings.get(["usb2"]),
			usb3 =                                self._settings.get(["usb3"]),
			usb4 =                                self._settings.get(["usb4"]),
			usb5 =                                self._settings.get(["usb5"]),
			init =                                self._settings.get(["init"])
		)

	def get_template_configs(self):
		return [dict(type="settings", custom_bindings=False)]

	def get_assets(self):
		return dict(
			js =                                  ["js/usbcontrol.js"],
			css =                                 ["css/usbcontrol.css"],
			less =                                ["less/usbcontrol.less"]
		)

	def get_api_commands(self):
		return dict(usb2=["arg2"],usb3=["arg3"],usb4=["arg4"],usb5=["arg5"],save=["init"])

	def on_api_command(self, command, data):
		import flask
		uhubctlFolder =                         "/home/pi/oprint/lib/python2.7/site-packages/usbcontrol/bin"
		if command == "save":
			self._logger.info("save init in settings")
			s =                                   settings()
			s.setBoolean(["plugins", "usbcontrol", "init"], True)
			s.save()
		if command == "usb2":
			strArg2 =                             "{arg2}".format(**data)
			try:
				self._logger.info("usb2 `{}`...".format(strArg2))
				output =                            call(["sudo", "./uhubctl", "--loc=1-1", "--ports=2", "--action=" + strArg2], cwd=uhubctlFolder)
				if output > 0:
					self._logger.info("  uhubctrl returned: {}".format(output))
			except OSError as e:
				self._logger.info("uhubctl failed, throwing error")
				output =                            "N/A"
		if command == "usb3":
			strArg3 =                             "{arg3}".format(**data)
			try:
				self._logger.info("usb3 `{}`...".format(strArg3))
				output =                            call(["sudo", "./uhubctl", "--loc=1-1", "--ports=3", "--action=" + strArg3], cwd=uhubctlFolder)
				if output > 0:
					self._logger.info("  uhubctrl returned: {}".format(output))
			except OSError as e:
				self._logger.info("uhubctl failed, throwing error")
				output =                            "N/A"
		if command == "usb4":
			strArg4 =                             "{arg4}".format(**data)
			try:
				self._logger.info("usb4 `{}`...".format(strArg4))
				output =                            call(["sudo", "./uhubctl", "--loc=1-1", "--ports=4", "--action=" + strArg4], cwd=uhubctlFolder)
				if output > 0:
					self._logger.info("  uhubctrl returned: {}".format(output))
			except OSError as e:
				self._logger.info("uhubctl failed, throwing error")
				output =                            "N/A"
		if command == "usb5":
			strArg5 =                             "{arg5}".format(**data)
			try:
				self._logger.info("usb5 `{}`...".format(strArg5))
				output =                            call(["sudo", "./uhubctl", "--loc=1-1", "--ports=5", "--action=" + strArg5], cwd=uhubctlFolder)
				if output > 0:
					self._logger.info("  uhubctrl returned: {}".format(output))
			except OSError as e:
				self._logger.info("uhubctl failed, throwing error")
				output =                            "N/A"

	def on_startup(self, host, port):
		pass

	def get_update_information(self):
		return dict(
			usbcontrol=dict(
				displayName =                       "Usbcontrol Plugin",
				displayVersion =                    self._plugin_version,
				type =                              "github_release",
				user =                              "OutsourcedGuru",
				repo =                              "OctoPrint-USBControl",
				current =                           self._plugin_version,
				pip =                               "https://github.com/OutsourcedGuru/OctoPrint-USBControl/archive/{target_version}.zip"
			)
		)

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ =               UsbcontrolPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

