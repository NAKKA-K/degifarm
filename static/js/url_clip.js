<script>
    const clipTeacher = function(){
        const url = document.getElementById('teacher_link');
        url.select();
        document.execCommand('copy');
    }

    const clipStudent = function(){
        const url = document.getElementById('student_link');
        url.select();
        document.execCommand('copy');
    }
</script>

