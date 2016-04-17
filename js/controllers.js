const MODE_MOBILE = 0;
const MODE_MEDIUM = 1;
const MODE_DESKTOP = 2;

angular.module( 'mainapp.controllers', [] )

.controller( 'HomeCtrl', function( $scope ) {
    const vm = this;

    vm.determineWindowMode = determineWindowMode;

    $scope.Anthony = {};
    $scope.Guillaume = {};
    $scope.Daniel = {};
    $scope.Anders = {};
    $scope.Brian = {};


    $scope.Anthony.fullname = 'Anthony Altieri';
    $scope.Anthony.phonenum = '(818) 201-4755';
    $scope.Anthony.email = 'AnthonyRAltieri@gmail.com';
    $scope.Anthony.githublink = 'github.com/AnthonyAltieri';
    $scope.Anthony.bio = 'I am a fourth year pre-law student at the University'
        + 'of California, San Diego studying Computer Science Engineering. My '
        + 'interests include computer science, programming, finance, and law. I'
        + ' am mostly a front-end developer but I am capable of all facets of '
        + 'development. I am currently an intern at the startup Mesh for which '
        + 'I do front-end development. I am also the founder/owner/front-end '
        + 'developer for Stylist Spaces a marketing product for hairstylists.';


    $scope.Guillaume.fullname = 'Guillaume Hauss';
    $scope.Guillaume.phonenum = '(858) 997-7931';
    $scope.Guillaume.email = 'ghauss@hotmail.fr';
    $scope.Guillaume.githublink = 'github.com/GuillaumeHauss';
    $scope.Guillaume.bio = 'I am a french engineering student, majoring in '
        + "Computer Science and Automation in Robotics. I've been in San Diego "
        + 'since December and will leave this little heaven in June. I am a '
        + 'project-driven guy, always looking for solutions whenever there is '
        + 'a problem. I like working in team and be part of something bigger. '
        + 'I was the CEO of an engineering consulting cabinet in Nantes, for 1 '
        + 'year. I managed 32 co-workers and went over 20 projects as Program '
        + 'Manager. I like new technologies and especially connected cars.';

    $scope.Daniel.fullname = 'Daniel Kong';
    $scope.Daniel.phonenum = '(310) 985-1473';
    $scope.Daniel.email = 'dakong94@gmail.com';
    $scope.Daniel.githublink = 'github.com/dakong';
    $scope.Daniel.bio = "Hey there! I'm Fourth year Computer Science major at UC "
        + 'San Diego,interested in front end web development. Some of my hobbies '
        + 'include gaming, hiking, and snowboarding. I currently work at UC San '
        + 'Diego Creative Service & Publications, as a Student Web Developer.';

    $scope.Anders.fullname = 'Anders Trier';
    $scope.Anders.phonenum = '-';
    $scope.Anders.email = '-';
    $scope.Anders.githublink = 'github.com/AndersTrier';
    $scope.Anders.bio = 'First year graduate student. Interested in Computer Security.';


    $scope.Brian.fullname = 'Brian Kim';
    $scope.Brian.phonenum = '(818) 276-7028';
    $scope.Brian.email = 'brianskiim@gmail.com';
    $scope.Brian.githublink = 'github.com/brianskiim';
    $scope.Brian.bio = 'Hello. I am a fourth year Computer Science student at UCSD. I '
        + "prefer front end development because I don't have much backend knowledge. "
        + 'On my free time I enjoy playing basketball, going to the gym, and any car '
        + 'related activities. I currently work for Hush doing all sorts of things.';



    function determineWindowMode() {
        const width = window.innerWidth;
        if ( width < 768 ) {
            return MODE_MOBILE;
        } else if ( width < 991 ) {
            return MODE_MEDIUM;
        } else {
            return MODE_LARGE;
        }
    }
});

