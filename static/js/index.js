$('#signin button').click(function() {
	$.getJSON('/api/signin?callback=?', {email: $('#signin-email').val(), password: $('#signin-password').val()}, function(response) {
		if (response.success) {
			alert('logged in');
		} else {
			$('#signin .error').text(response.error);
		}
	});
});