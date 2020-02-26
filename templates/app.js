<button id="rzp-button1">Pay</button>
<script src="https://checkout.razorpay.com/v1/checkout.js"></script>
<script>
var options = {
    "key": "{{key_id}}", // Enter the Key ID generated from the Dashboard
    "order_id": "{{order_id}}",
    "amount": "{{amount}}", // Amount is in currency subunits. Default currency is INR. Hence, 50000 means 50000 paise or ₹500.
    "currency": "{{currency}}",
    "name": "Acme Corp",
    "description": "A Wild Sheep Chase is the third novel by Japanese author  Haruki Murakami",
    "image": "https://example.com/your_logo",
    "callback_url": "http://127.0.0.1:5000/charge",
    "prefill": {
        "name": "Gaurav Kumar",
        "email": "gaurav.kumar@example.com",
        "contact": "9999999999"
    },
    "notes": {
        "address": "note value"
    },
    "theme": {
        "color": "#F37254"
    }
};
var rzp1 = new Razorpay(options);
document.getElementById('rzp-button1').onclick = function(e){
    rzp1.open();
    e.preventDefault();
}
</script>