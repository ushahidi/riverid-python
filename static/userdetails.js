(function() {
	var user_id = localStorage.getItem('user_id');
	var session_id = localStorage.getItem('session_id');
	if (user_id == null || session_id == null) {
		alert('Not signed in.');
	} else {
		alert(user_id + ' ' + session_id);
	}
})();