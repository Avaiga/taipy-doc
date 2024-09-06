---
hide:
  - toc
---
Taipy provides a way to inform users that some action is taking place
as an informative message that does not impact the user interaction.

Notifications can be triggered at any time to send a temporary message
to the user, using the `notify()^` function.<br/>
One can specify how long the message remains visible on the screen.
The default duration of how long the message is visible can be set using the
[*notification_duration*](../advanced_features/configuration/gui-config.md#p-notification_duration) configuration setting.

A notification is a short message that appears in a small popup window.
The level of urgency of the message is reflected in the color of that window.

If permission is given to the browser, notifications can also appear directly
on the desktop of the user's machine.<br/>
The [*system_notification*](../advanced_features/configuration/gui-config.md#p-system_notification) configuration setting
can prevent that behavior.

