function courseAdd() {
    const courseInput = document.getElementById('addCourse');
    var course = courseInput.value.trim();
    if (course) {
        // Convert to capitals
        course = course.replace(/ +/g, '');
        course = course.toUpperCase();

        // Update course select
        const courseSelect = document.getElementById('course');
        const courseOption = document.createElement('option');
        courseOption.text = course;
        courseOption.value = course;
        courseSelect.add(courseOption);
        courseInput.value = '';
    }
}
