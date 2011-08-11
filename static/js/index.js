$('nav a').live('click', function() {
	$('nav a.active').removeClass('active');
	$(this).addClass('active');
	$('section').hide();
	$('#' + this.hash.substr(1)).show();
	return false;
});
$('#signin button').live('click', function() {
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

	return false;
});
$('#register button').live('click', function() {
	if ($('#register-email').val() == $('#register-confirm').val()) {
		$('#register button, #register input').attr('disabled', true);

		$.getJSON('/api/requestpassword?callback=?', {email: $('#register-email').val()}, function(response) {
			if (response.success) {
				$('#register .error').text('');
				$('#register .success').show();
				$('#register input').val('');
			} else {
				$('#register .success').hide();
				$('#register .error').text(response.error);
			}

			$('#register button, #register input').attr('disabled', false);
		});
	} else {
		$('#register .error').text('The two email addresses you entered do not match. Please try again.')
	}

	return false;
});
