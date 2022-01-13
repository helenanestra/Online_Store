    $(document).ready(function() {
    // all your jquery/javascript has to be in this block: if you are using jquery
            var modal = document.getElementById("myModal");
            var modalImg = document.getElementById("img01");
            var captionText = document.getElementById("caption");
            $('.product').click(function() {
                modal.style.display = "block";
                modalImg.src = $(this).attr('src');
                captionText.innerHTML = $(this).attr('alt');
            });
            $('.close').click(function() {
                modal.style.display = "none";
            });
    });