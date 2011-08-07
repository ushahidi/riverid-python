$('#signin button').click(function() {
	$('#signin button, #signin input').attr('disabled', true);
	$.getJSON('/api/signin?callback=?', {email: $('#signin-email').val(), password: $('#signin-password').val()}, function(response) {
		if (response.success) {
			localStorage.setItem('session_email', $('#signin-email').val());
			localStorage.setItem('session_id', response.response);
			$('#email').text($('#signin-email').val());
			$('#signout').show();
			$('#anonymous, #signin').hide();
			$('#signedin').show();
		} else {
			$('#signin .error').text(response.error);
		}
		$('#signin button, #signin input').attr('disabled', false);
	});
});
