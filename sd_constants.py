class constants:
    class error:
        STATUS_DEMO = 1;
        OPENING_MODULE = -8000;
        SING_MODULE = -8001;
        OPENING_HVI = -8002;
        CLOSING_HVI = -8003;
        MODULE_NOT_OPENED = -8004;
        MODULE_NOT_OPENED_BY_USER = -8005;
        MODULE_ALREADY_OPENED = -8006;
        HVI_NOT_OPENED = -8007;
        INVALID_OBJECTID = -8008;
        INVALID_MODULEID = -8009;
        INVALID_MODULEUSERNAME = -8010;
        INVALID_HVIID = -8011;
        INVALID_OBJECT = -8012;
        INVALID_NCHANNEL = -8013;
        BUS_DOES_NOT_EXIST = -8014;
        BITMAP_ASSIGNED_DOES_NOT_EXIST = -8015;
        BUS_INVALID_SIZE = -8016;
        BUS_INVALID_DATA = -8017;
        INVALID_VALUE = -8018;
        CREATING_WAVE = -8019;
        NOT_VALID_PARAMETERS = -8020;
        AWG_FAILED = -8021;
        DAQ_INVALID_FUNCTIONALITY = -8022;
        DAQ_POOL_ALREADY_RUNNING = -8023;
        UNKNOWN = -8024;
        INVALID_PARAMETERS = -8025;
        MODULE_NOT_FOUND = -8026;
        DRIVER_RESOURCE_BUSY = -8027;
        DRIVER_RESOURCE_NOT_READY = -8028;
        DRIVER_ALLOCATE_BUFFER = -8029;
        ALLOCATE_BUFFER = -8030;
        RESOURCE_NOT_READY = -8031;
        HARDWARE = -8032;
        INVALID_OPERATION = -8033;
        NO_COMPILED_CODE = -8034;
        FW_VERIFICATION = -8035;
        COMPATIBILITY = -8036;
        INVALID_TYPE = -8037;
        DEMO_MODULE = -8038;
        INVALID_BUFFER = -8039;
        INVALID_INDEX = -8040;
        INVALID_NHISTOGRAM = -8041;
        INVALID_NBINS = -8042;
        INVALID_MASK = -8043;
        INVALID_WAVEFORM = -8044;
        INVALID_STROBE = -8045;
        INVALID_STROBE_VALUE = -8046;
        INVALID_DEBOUNCING = -8047;
        INVALID_PRESCALER = -8048;
        INVALID_PORT = -8049;
        INVALID_DIRECTION = -8050;
        INVALID_MODE = -8051;
        INVALID_FREQUENCY = -8052;
        INVALID_IMPEDANCE = -8053;
        INVALID_GAIN = -8054;
        INVALID_FULLSCALE = -8055;
        INVALID_FILE = -8056;
        INVALID_SLOT = -8057;
        INVALID_NAME = -8058;
        INVALID_SERIAL = -8059;
        INVALID_START = -8060;
        INVALID_END = -8061;
        INVALID_CYCLES = -8062;
        HVI_INVALID_NUMBER_MODULES = -8063;

        @classmethod
        def getErrorMessage(cls, errorNumber) :
            cls._SD_Object__core_dll.SD_GetErrorMessage.restype = c_char_p;
            return cls._SD_Object__core_dll.SD_GetErrorMessage(errorNumber).decode();
    class object_type:
        HVI = 1;
        AOU = 2;
        TDC = 3;
        DIO = 4;
        WAVE = 5;
        AIN = 6;
        AIO = 7;

    class wave_shapes:
        AOU_HIZ = -1;
        AOU_OFF = 0;
        AOU_SINUSOIDAL = 1;
        AOU_TRIANGULAR = 2;
        AOU_SQUARE = 4;
        AOU_DC = 5;
        AOU_AWG = 6;
        AOU_PARTNER = 8;

    class waveform_types :
        WAVE_ANALOG = 0;
        WAVE_IQ = 2;
        WAVE_IQPOLAR = 3;
        WAVE_DIGITAL = 5;
        WAVE_ANALOG_DUAL = 7;

    class modulation_types :
        AOU_MOD_OFF = 0;
        AOU_MOD_FM = 1;
        AOU_MOD_PHASE = 2;

        AOU_MOD_AM = 1;
        AOU_MOD_OFFSET = 2;

    class trigger_directions:
        AOU_TRG_OUT = 0;
        AOU_TRG_IN = 1;

    class trigger_behaviors:
        TRIGGER_NONE = 0;
        TRIGGER_HIGH = 1;
        TRIGGER_LOW = 2;
        TRIGGER_RISE = 3;
        TRIGGER_FALL = 4;

    class marker_modes:
        DISABLED = 0;
        START = 1;
        START_AFTER_DELAY = 2;
        EVERY_CYCLE = 3;
        END = 4;

    class trigger_value:
        LOW = 0;
        HIGH = 1;

    class sync_modes:
        SYNC_NONE = 0;
        SYNC_CLK10 = 1;

    class reset_mode:
        LOW = 0;
        HIGH = 1;
        PULSE = 2;

    class address_mode:
        AUTOINCREMENT  = 0;
        FIXED = 1;

    class access_mode:
        NONDMA = 0;
        DMA = 1;

    class trigger_modes:
        AUTOTRIG = 0;
        VIHVITRIG = 1;
        SWHVITRIG = 1;
        EXTTRIG = 2;
        ANALOGTRIG = 3;
        SWHVITRIG_CYCLE = 5;
        EXTTRIG_CYCLE = 6;
        ANALOGAUTOTRIG = 7;

    class trigger_external_sources:
        TRIGGER_EXTERN = 0;
        TRIGGER_PXI = 4000;
        TRIGGER_PXI0 = 4000;
        TRIGGER_PXI1 = 4001;
        TRIGGER_PXI2 = 4002;
        TRIGGER_PXI3 = 4003;
        TRIGGER_PXI4 = 4004;
        TRIGGER_PXI5 = 4005;
        TRIGGER_PXI6 = 4006;
        TRIGGER_PXI7 = 4007;

    class io_directions:
        DIR_IN = 0;
        DIR_OUT = 1;

    class pin_directions:
        DIR_IN = 0;
        DIR_OUT = 1;

    class strobe:
        STROBE_OFF = 0;
        STROBE_ON = 1;

        STROBE_LEVEL = 2;##0b10;
        STROBE_EDGERISE = 1;
        STROBE_EDGEFALL = 0;

    class debouncing_types:
        DEBOUNCING_NONE = 0;
        DEBOUNCING_LOW = 2;##0b10;
        DEBOUNCING_HIGH = 3;##0b11;

    class dio_bus:
        DIO_INPUT_BUS0 = 1000;
        DIO_INPUT_BUS1 = 1001;
        DIO_OUTPUT_BUS0 = 2000;
        DIO_OUTPUT_BUS1 = 2001;

    class compatibility:
        LEGACY = 0;
        KEYSIGHT = 1;


