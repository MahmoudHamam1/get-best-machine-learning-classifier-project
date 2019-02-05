$(function(){
	
	get_scores()
	get_table()
})

function get_scores(){
	$.ajax({
        url: 'http://127.0.0.1:9090/compare/score',
        type: 'get',
        data: {},
		contentType:"application/json",
	    dataType:'json',
		jsonp: false,
        beforeSend: function() {
            
        },
        success: function(data) {
			$(".LOG_head span").html(data["LOGR_score"]);
			$(".KNN_head span").html(data["KNN_score"]);
			$(".RF_head span").html(data["RF_score"]);
			$(".SVM_head span").html(data["SVM_score"]);
			$(".naiv_head span").html(data["naiv_score"]);
			$(".Dtree_head span").html(data["Dtree_score"]);
        }
       
    });
	
}

function get_table(){
	$.ajax({
        url: 'http://127.0.0.1:9090/',
        type: 'get',
        data: {},
		contentType:"application/json",
	    dataType:'json',
		jsonp: false,
        beforeSend: function() {
            
        },
        success: function(data) {
			res=JSON.parse(data["data"])
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