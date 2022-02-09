{
  'targets': [
    {
      'target_name': "binding",
      'sources': ["binding.cc"],
#      'includes': ["../common.gypi"],
    },
  ],
  'defines': ["V8_DEPRECATION_WARNINGS=1"],
  'conditions': [
    [
      'OS in "linux freebsd openbsd solaris android aix cloudabi"',
      {
        'cflags': ["-Wno-cast-function-type"],
      },
    ],
  ],
}