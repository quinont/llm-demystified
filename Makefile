APP_DIR = 00_setup/02_entorno_python

%:
	$(MAKE) -C $(APP_DIR) $(MAKECMDGOALS)

.PHONY: install active
