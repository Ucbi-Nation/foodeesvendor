function payWithPaystack() {

    var handler = PaystackPop.setup({
        key: 'pk_test_a2974e4c99f2926268ce27cba32614b42b882e77', //put your public key here
        email: document.getElementById("email").value, //put your customer's email here
        amount: document.getElementById("amount").value * 100, //amount the customer is supposed to pay
        firstname: document.getElementById("name").value,
        metadata: {
            custom_fields: [
                {
                    display_name: "Mobile Number",
                    variable_name: "mobile_number",
                    value: document.getElementById("phone_number").value //customer's mobile number
                }
            ]
        },

        callback: function(response){
      	var message = 'Payment Reference: is' + response.reference + '\n Click ok to process';
      	if(response.status == "success")
      		alert(message);
      		submitFormData();
    	},
        onClose: function () {
            //when the user close the payment modal
            alert('Transaction cancelled');
        }
    });
    handler.openIframe(); //open the paystack's payment modal
}