<script>
    function likeOrUnlike(id, postLiked){
        const btn = document.getElementById(`${id}`);

        btn.classList.remove('fa-thumbs-up')
        btn.classList.remove('fa-thumbs-down')

        if(postLiked.indexOf(id) >= 0){
            var liked = true;
        }else{
            var liked = false;
        }

        if(liked === true){
            fetch(`/unlike/${id}`)
            .then(response => response.json)
            .then(result => {
                btn.classList.add("fa-thumbs-up")
            })
        }else{
            fetch(`/like/${id}`)
            .then(response => response.json)
            .then(result => {
                btn.classList.add("fa-thumbs-down")
            })
        }
        liked = !liked
    }
</script>