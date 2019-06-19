$(function(){
      var error_name=false;
      var error_pwd=false;

      $('#user_name').blur(function() {
		check_user_name();
	});

      $('#pwd').blur(function() {
		check_pwd();
	});
      function check_user_name(){
		if (error_name == 1){
          $('#name_input').next().html('用户名错误').show();
        }
	}
	  function check_pwd(){
          if ( error_pwd == 1){
          $('#pass_input').next().html('用户名错误').show();
        }
	}
});
