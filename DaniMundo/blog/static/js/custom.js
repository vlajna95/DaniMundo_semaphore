function checkAnswer(origin, correct_answer_message="Bravo!", wrong_answer_message="Hmmm... no.") {
var question_name = $(origin).attr("data-question");
var correct_answer_element = $(origin).attr("data-correct");
var correct_answer_id = $("#"+correct_answer_element).val();
var correct_answer_label = $("label[for='"+correct_answer_id+"']").text();
var chosen_answer_id = $("input[name='"+question_name+"']:checked").attr("id");
var chosen_answer_label = $("label[for='"+chosen_answer_id+"']").text();
if(correct_answer_id == chosen_answer_id) {
alert(correct_answer_message);
}
else {
alert(wrong_answer_message + " \n" + correct_answer_label);
}
$("input[name="+question_name+"]").attr("disabled", true);
}
