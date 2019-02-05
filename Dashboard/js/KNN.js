$(function(){
	
	get_scores()
	
	$(".card-body form").on("submit",function(e){
		e.preventDefault()
		get_predection(1)
	})
	
	$("#predectTest").on("click",function(e){
		e.preventDefault()
		get_predection(0)
	})
	
})

function get_scores(){
	$.ajax({
        url: 'http://127.0.0.1:9090/KNN/score',
        type: 'get',
        data: {},
		contentType:"application/json",
	    dataType:'json',
		jsonp: false,
        beforeSend: function() {
            
        },
        success: function(data) {
			$(".alert .score").html(data["score"]);
        }
       
    });
	
}

function get_predection(flag){
	/*df = $(".predetion .custom-file-input")
	console.log(df)*/
	$.ajax({
        url: 'http://127.0.0.1:9090/KNN/predect',
        type: 'get',
        data: {"flag":flag,
		"customerID":$(".card-body form input[name='customerID']").val(),
		"Gender":$(".card-body form input[name='Gender']").val(),
		"SeniorCitizen":$(".card-body form input[name='SeniorCitizen']").val(),
		"Partner":$(".card-body form input[name='Partner']").val(),
		"Dependents":$(".card-body form input[name='Dependents']").val(),
		"tenure":$(".card-body form input[name='tenure']").val(),
		"PhoneService":$(".card-body form input[name='PhoneService']").val(),
		"MultipleLines":$(".card-body form input[name='MultipleLines']").val(),
		"InternetService":$(".card-body form input[name='InternetService']").val(),
		"OnlineSecurity":$(".card-body form input[name='OnlineSecurity']").val(),
		"OnlineBackup":$(".card-body form input[name='OnlineBackup']").val(),
		"DeviceProtection":$(".card-body form input[name='DeviceProtection']").val(),
		"TechSupport":$(".card-body form input[name='TechSupport']").val(),
		"StreamingTV":$(".card-body form input[name='StreamingTV']").val(),
		"StreamingMovies":$(".card-body form input[name='StreamingMovies']").val(),
		"Contract":$(".card-body form input[name='Contract']").val(),
		"PaperlessBilling":$(".card-body form input[name='PaperlessBilling']").val(),
		"BaymentMrthod":$(".card-body form input[name='BaymentMrthod']").val(),
		"MonthlyCharges":$(".card-body form input[name='MonthlyCharges']").val(),
		"TotalCharges":$(".card-body form input[name='TotalCharges']").val(),
		},
		contentType:"application/json",
	    dataType:'json',
		jsonp: false,
        beforeSend: function() {
            
        },
        success: function(data) {
			
			res=JSON.parse(data["pred"])
			arr=[]
			$.each(res, function(index, val) {
                $('table thead tr').append('<th>' + index + '</th>');
				arr.push(index)
            });
			
			$.each(res[arr[0]], function(index, val) {
				txt="";
				$.each(arr, function(i ,v) {
					txt+="<td>"+res[v][index]+"</td>"
				});
                $('table tbody').append('<tr>' + txt + '</tr>');
				
            });
			 $("#example1").DataTable();
        }
       
    });
	
}