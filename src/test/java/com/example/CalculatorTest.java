package com.example;

import junit.framework.TestCase;
import org.junit.Test;

public class CalculatorTest extends TestCase {

    private final Calculator calculator = new Calculator();

    @Test
    public void testSubtract() {
        System.out.println("Running testSubtract");
        assertEquals(1, calculator.subtract(3, 2));
    }
}