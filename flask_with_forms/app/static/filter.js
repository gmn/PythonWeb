
/**
 * simple client-side mechanism to filter the requests shown by Client
 */
document.getElementById('client_filter').onchange = function() {
    $(".request").hide();
    var client = $("#client_filter option:selected").val();
    $(client).show();
    var msg = $("#filter_msg")
    if ( client == ".request" ) {
        msg.html("Showing requests for all Clients")
    } else {
        msg.html("Showing requests for Client " + client.charAt(1) + " only");
    }
}

