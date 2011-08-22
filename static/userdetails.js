(function() {
	var user_id = $.cookie('user_id');
	var session_id = $.cookie('session_id');
	if (user_id == null || session_id == null) {
		alert('Not signed in.');
	} else {
		alert(user_id + ' ' + session_id);
	}
})();