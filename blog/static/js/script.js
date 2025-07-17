$(document).ready(function () {
  $("#registerForm").validate({
    rules: {
      username: {
        required: true,
      },
      email: {
        required: true,
        email: true,
      },
      password: {
        required: true,
        minlength: 8,
        maxlength: 15,
      },
      phone_no: {
        required: true,
        digits: true,
        minlength: 10,
        maxlength: 12,
        pattern: /^[0-9]{10}$/
      },
    },
    messages: {
      username: {
        required: "Please Enter username",
      },
      email: {
        required: "Please Enter Email",
        email: "Please Enter valid Email",
      },
      password: {
        required: "Please Enter password",
        minlength: "Password must atleast 8 characters",
        maxlength: "Password must below 15 characters",
      },
      phone_no: {
        required: "Please Enter phone No",
        digits: "enter valid number",
        minlength: "phone no must  10 digits",
        maxlength: "phone no must below 12 digits",
        pattern: 'Enter valid number'
      },
    },
    submitHandler: function (form) {
      form.submit();
    },
  });
});
