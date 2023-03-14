## RNode Bluetooth-Einrichtung für Sideband auf Android

In dieser kurzen Anleitung werden alle notwendigen Schritte zur Einrichtung eines RNode für die Verwendung mit der Sideband-Anwendung auf Android-Geräten beschrieben.



# Ersteinrichtung und Bluetooth-Kopplung
Um einen RNode über Bluetooth mit einem Android-Gerät zu verwenden, muss zunächst eine normale Bluetooth-Kopplung zwischen den Geräten durchgeführt werden. Hier ist die korrekte Vorgehensweise:

Verbinden Sie den RNode über USB mit Ihrem Android-Gerät. Warten Sie, bis der Android-Berechtigungsdialog erscheint, und erteilen Sie Sideband die USB-Berechtigung für den Anschluss. Wenn diese Berechtigung nicht speziell für Sideband erteilt wird, kann die Sideband App nicht mit dem Anschluss kommunizieren.
Standardmäßig ist Bluetooth auf einem RNode ausgeschaltet. Wenn Sie Bluetooth auf Ihrem RNode noch nicht eingeschaltet haben, gehen Sie wie folgt vor:
Gehen Sie in der Sideband App zu Hardware > RNode und drücken Sie die Schaltfläche Bluetooth aktivieren. Das Bluetooth-Symbol auf dem RNode-Display sollte nun aktiv werden.
Drücken Sie dann die Taste Start Pairing Mode. Das Bluetooth-Symbol sollte sich ändern, um anzuzeigen, dass sich der RNode jetzt im Kopplungsmodus befindet.
Sie können nun ein normales Bluetooth-Pairing zwischen dem RNode und Ihrem Gerät durchführen:
Gehen Sie zu den Bluetooth-Einstellungen Ihres Android-Geräts und starten Sie die Kopplung eines neuen Geräts. Der RNode sollte erkannt werden, und wenn Sie ihn für die Kopplung auswählen, wird der RNode seinen Kopplungscode auf dem Display anzeigen. Überprüfen Sie, ob der Code übereinstimmt und akzeptieren Sie die Kopplung von Ihrem Android-Gerät.
Der Kopplungsvorgang ist nun abgeschlossen, und Sideband kann das RNode verwenden.
Stellen Sie sicher, dass Sie Sideband die Erlaubnis erteilen, sich mit Bluetooth-Geräten zu verbinden, wenn Sie dazu aufgefordert werden. Wenn Sie versehentlich die erforderlichen Berechtigungen verweigern, müssen Sie sie möglicherweise manuell in den Einstellungen Ihres Geräts aktivieren.
Sie müssen den RNode nicht manuell in den Bluetooth-Einstellungen Ihres Geräts verbinden, wenn Sie ihn verwenden möchten. Sideband initiiert die Bluetooth-Verbindung selbst, wenn es den RNode verwenden möchte.
Einrichtung in Sideband

# Um den gekoppelten RNode im Seitenband zu verwenden, müssen die folgenden Schritte durchgeführt werden:

Gehen Sie zu Hardware > RNode und stellen Sie sicher, dass gültige Funkparameter konfiguriert wurden. Die App bietet sinnvolle Standardwerte für die meisten Parameter, aber Sie müssen zumindest eine gültige Frequenz für das Gerät angeben.
Vergewissern Sie sich, dass das Kontrollkästchen Über Bluetooth verbinden aktiviert ist.
Vergewissern Sie sich im Programmteil Konnektivität, dass das Kontrollkästchen Über RNode verbinden aktiviert ist. Sie können hier optional IFAC-Parameter für Ihr Netzwerk angeben.
Fahren Sie Sideband vollständig herunter (Menü > Herunterfahren) und starten Sie es neu. Sie sollten nun sehen, dass Sideband startet und sich mit Ihrem RNode verbindet.
Im Dialogfeld "Verbindungsstatus" sollte der RNode als "On-Air" angezeigt werden.
Das war's dann auch schon. Sobald das Pairing abgeschlossen ist und die RNode-Schnittstelle in Sideband aktiviert wurde, wird sie verbunden und verwendet, sobald der RNode eingeschaltet und in Reichweite ist.

Um die Sideband App vorübergehend davon abzuhalten, den RNode zu verwenden, können Sie in den Abschnitt Hardware > RNode des Programms gehen und die Option Über Bluetooth verbinden deaktivieren. Diese Änderung erfordert keinen Neustart des Programms, um wirksam zu werden.

Es ist auch erwähnenswert, dass die 1.x-Versionen der Firmware nur eine Host-Verbindung zur gleichen Zeit zulassen. Sie können nicht gleichzeitig über USB/Seriell von einem Computer und über Bluetooth von einem anderen Gerät aus verbunden sein. Der RNode schaltet die Host-Verbindung so um, dass immer nur eine verwendet wird.

Wenn Sie das Gerät über Bluetooth verwenden, müssen Sie es nur mit Strom versorgen, entweder über den USB-Anschluss oder eine Batterie, aber stellen Sie keine Verbindung über USB oder seriell her. Sie können es problemlos an den USB-Anschluss eines Computers anschließen, aber öffnen Sie es nicht mit rnsd oder etwas anderem.
