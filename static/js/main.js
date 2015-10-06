$('form[action="/accounts/register/"] #id_department').change(function() {
    if ($(this).val() == "Άλλο") {
        $('#id_student_id').val('-').parent().hide();
    }
    else {
        $('#id_student_id').val('').parent().show();
    }
});
$('form[action="/accounts/register/"] #id_department').change()
