$('document').ready(function(){
   $('.delete-confirm').on('click',function(e){
      e.preventDefault();
      var id = $(this).val();
      $('#delete_id').val(id);
      $('#deleteModal').modal('show'); 
   });
});