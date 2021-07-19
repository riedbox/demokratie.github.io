$(document).ready(function () {
	var idleTime = 0;
	// Increment the idle time counter every minute.
	var idleInterval = setInterval(function() {
	idleTime = idleTime + 1;
	console.log ("Checking inactivity " + idleTime);
	if (idleTime > 5) {
		console.log ("Redirecting");
		window.location = "/";
	}
	}, 60000); // 1 minute

	// Zero the idle timer on mouse movement.
	$(this).mousemove(function (e) {
		idleTime = 0;
	});
	$(this).keypress(function (e) {
		idleTime = 0;
	});
});