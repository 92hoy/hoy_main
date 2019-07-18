module.exports = function(grunt) {

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        clean: {
            dist: ['dist/*'],
            tmp : ['.tmp','**/.DS_store', 'dist/scripts']
        },
        copy: {
            modules:{
                files: [
                    {expand: true, cwd: 'node_modules', src: '<%= pkg.copy %>', dest: 'libs'}
                ]
            },
            dist: {
                files: [
                    {expand: true, cwd: 'html/', src: ['**'], dest: 'dist/html/'},
                    {expand: true, cwd: 'assets/', src: ['**', '!**/scss/**'], dest: 'dist/assets/'},
                    {expand: true, cwd: 'libs/', src: '**', dest: 'dist/libs/'},
                    {src: 'index.html', dest: 'dist/index.html'}
                ]
            },
            min: {
                files: [
                    {src: 'dist/scripts/app.min.js', dest : 'dist/html/scripts/app.min.js'}
                ]
            }
        },
        watch: {
            sass: {
              files: ['assets/css/scss/*.scss'],
              tasks: ['sass'],
            }
        },
        sass: {
            dist: {
                files: [
                    {'assets/css/app.css': ['assets/css/scss/app.scss']},
                    {'assets/css/app.rtl.css': ['assets/css/scss/app.rtl.scss']},
                    { expand: true, cwd: 'assets/css/scss/theme/', src: ['*.scss'], dest: 'assets/css/theme/', ext: '.css'}
                ]
            }
        },
        htmlmin: {
            dist: {
                options: { removeComments: true, collapseWhitespace: true },
                files: [
                    { expand: true, cwd: 'dist/html/', src: ['*.html', '**/*.html'], dest: 'dist/html/' }
                ]
            }
        },
        useminPrepare: {
            html: ['html/*.html'],
            options: {
              dest: 'dist'
            }
        },
        usemin: {
            html: ['dist/html/*.html']
        }
    });

    require('load-grunt-tasks')(grunt);

    grunt.registerTask('copy:libs', [
        'copy:modules'
    ]);

    grunt.registerTask('build:sass', [
        'sass'
    ]);

    grunt.registerTask('build:dist', [
        'clean:dist',
        'copy',
        'sass',
        'useminPrepare',
        'concat:generated',
        'cssmin:generated',
        'uglify:generated',
        'usemin',
        'htmlmin',
        'copy:min',
        'clean:tmp'
    ]);

};
