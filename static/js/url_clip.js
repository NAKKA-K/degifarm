function clipTeacher(){
    const url = document.getElementById('teacher_link');
    url.select();
    document.execCommand('copy');
}

function clipStudent(){
    const url = document.getElementById('student_link');
    url.select();
    document.execCommand('copy');
}
