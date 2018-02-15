$.ajax({
            url: 'http://127.0.0.1:8000/allCats',
            type: 'get',
            success: function (response) {
                data = JSON.parse(response);
                console.log(data)
                cats = $("#cats");
                cats.html("");
                $(data).each(function(){
                    cats.append(category(this.fields.cat_name));
                    //cats.append(br())
                });
            }
        });


function br() {
    return $("<br>")
}

function category(name) {
    // <a href="#" class="list-group-item active">Category 1</a>
    return $('<a href="#" class="list-group-item active">'+name+'</a>')
}

function post(data) {
    return $(' <div class="col-lg-9">\n' +
        '\n' +
        '            <div class="card mt-4">\n' +
        '                <img class="card-img-top img-fluid" src="http://placehold.it/900x400" alt="">\n' +
        '                <div class="card-body">\n' +
        '                    <h3 class="card-title">Product Name</h3>\n' +
        '                    <h4>$24.99</h4>\n' +
        '                    <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sapiente dicta fugit\n' +
        '                        fugiat hic aliquam itaque facere, soluta. Totam id dolores, sint aperiam sequi pariatur\n' +
        '                        praesentium animi perspiciatis molestias iure, ducimus!</p>\n' +
        '                    <span class="text-warning">&#9733; &#9733; &#9733; &#9733; &#9734;</span>\n' +
        '                    4.0 stars\n' +
        '                </div>\n' +
        '            </div>\n' +
        '            <!-- /.card -->\n' +
        '\n' +
        '            <div class="card card-outline-secondary my-4">\n' +
        '                <div class="card-header">\n' +
        '                    Product Reviews\n' +
        '                </div>\n' +
        '                <div class="card-body">\n' +
        '                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Omnis et enim aperiam inventore,\n' +
        '                        similique necessitatibus neque non! Doloribus, modi sapiente laboriosam aperiam fugiat laborum.\n' +
        '                        Sequi mollitia, necessitatibus quae sint natus.</p>\n' +
        '                    <small class="text-muted">Posted by Anonymous on 3/1/17</small>\n' +
        '                    <hr>\n' +
        '                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Omnis et enim aperiam inventore,\n' +
        '                        similique necessitatibus neque non! Doloribus, modi sapiente laboriosam aperiam fugiat laborum.\n' +
        '                        Sequi mollitia, necessitatibus quae sint natus.</p>\n' +
        '                    <small class="text-muted">Posted by Anonymous on 3/1/17</small>\n' +
        '                    <hr>\n' +
        '                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Omnis et enim aperiam inventore,\n' +
        '                        similique necessitatibus neque non! Doloribus, modi sapiente laboriosam aperiam fugiat laborum.\n' +
        '                        Sequi mollitia, necessitatibus quae sint natus.</p>\n' +
        '                    <small class="text-muted">Posted by Anonymous on 3/1/17</small>\n' +
        '                    <hr>\n' +
        '                    <a href="#" class="btn btn-success">Leave a Review</a>\n' +
        '                </div>\n' +
        '            </div>\n' +
        '            <!-- /.card -->\n' +
        '\n' +
        '        </div>')
}