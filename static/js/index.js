$('nav a').live('click', function() {
	$('nav a.active').removeClass('active');
	$(this).addClass('active');
	$('section').hide("slide", {direction: "left"}, 1000);
	$('#' + this.hash.substr(1)).show();
	
	return false;
});

$('#signin button').live('click', function() {
	$('#signin button, #signin input').attr('disabled', true);

	$.getJSON('/api/signin', {email: $('#signin-email').val(), password: $('#signin-password').val()}, function(response) {
		if (response.success) {
			localStorage.setItem('session_email', $('#signin-email').val());
			localStorage.setItem('session_id', response.response);

			$('#email').text($('#signin-email').val());
			$('#anonymous, #signin').hide();
			$('#signedin, #changepassword').show();
			$('#signout').css('visibility', 'visible');
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

		$.getJSON('/api/registered', {email: $('#register-email').val()}, function(response) {
			if (!response.response) {
				$.getJSON('/api/requestpassword', {email: $('#register-email').val()}, function(response) {
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
				$('#register .success').hide();
				$('#register .error').text('This email address has already been registered.');
				$('#register button, #register input').attr('disabled', false);
			}
		});
	} else {
		$('#register .error').text('The two email addresses you entered do not match. Please try again.')
	}

	return false;
});

$('#recover button').live('click', function() {
	$('#recover button, #recover input').attr('disabled', true);

	$.getJSON('/api/registered', {email: $('#recover-email').val()}, function(response) {
		if (response.response) {
			$.getJSON('/api/requestpassword', {email: $('#recover-email').val()}, function(response) {
				if (response.success) {
					$('#recover .error').text('');
					$('#recover .success').show();
					$('#recover input').val('');
				} else {
					$('#recover .success').hide();
					$('#recover .error').text(response.error);
				}
				
				$('#recover button, #recover input').attr('disabled', false);
			});
		} else {
			$('#recover .success').hide();
			$('#recover .error').text('This email address is not currently associated with any account on our records.');
			$('#recover button, #recover input').attr('disabled', false);
		}
	});

	return false;
});

$('#changepassword button').live('click', function() {
	if ($('#changepassword-new').val() == $('#changepassword-confirm').val()) {
		$('#changepassword button, #changepassword input').attr('disabled', true);

		var params = {};
		params.email = localStorage.getItem('session_email');
		params.oldpassword = $('#changepassword-old').val();
		params.newpassword = $('#changepassword-new').val();

		$.getJSON('/api/changepassword', params, function(response) {
			if (response.success) {
				$('#changepassword .error').text('');
				$('#changepassword .success').show();
				$('#changepassword input').val('');
			} else {
				$('#changepassword .success').hide();
				$('#changepassword .error').text(response.error);
			}

			$('#changepassword button, #changepassword input').attr('disabled', false);
		});
	} else {
		$('#changepassword .error').text('The two passwords you entered do not match. Please try again.');
	}

	return false;
});

$('#changeemail button').live('click', function() {
	if ($('#changeemail-email').val() == $('#changeemail-confirm').val()) {
		$('#changeemail button, #changeemail input').attr('disabled', true);

		var params = {};
		params.oldemail = localStorage.getItem('session_email');
		params.newemail = $('#changeemail-email').val();
		params.password = $('#changeemail-password').val();

		$.getJSON('/api/changeemail', params, function(response) {
			if (response.success) {
				localStorage.setItem('session_email', $('#changeemail-email').val());
				$('#changeemail .error').text('');
				$('#changeemail .success').show();
				$('#changeemail input').val('');
			} else {
				$('#changeemail .success').hide();
				$('#changeemail .error').text(response.error);
			}

			$('#changeemail button, #changeemail input').attr('disabled', false);
		});
	} else {
		$('#changeemail .error').text('The two email addresses you entered do not match. Please try again.');
	}

	return false;
});
