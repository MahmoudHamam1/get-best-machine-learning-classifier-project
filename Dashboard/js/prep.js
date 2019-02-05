$(function(){
	
	get_prep()
	
	
	
})


function get_prep(){
	/*df = $(".predetion .custom-file-input")
	console.log(df)*/
	$.ajax({
        url: 'http://127.0.0.1:9090/prep',
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